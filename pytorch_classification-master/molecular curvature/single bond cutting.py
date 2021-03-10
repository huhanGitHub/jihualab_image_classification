from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw.MolDrawing import MolDrawing, DrawingOptions #Only needed if modifying defaults
opts = DrawingOptions()
opts.includeAtomNumbers = True

def findsinglebond():
    mols = []
    # smi = 'CC(C)OC(=O)C(C)NP(=O)(OCC1C(C(C(O1)N2C=CC(=O)NC2=O)(C)F)O)OC3=CC=CC=C3'
    smi = 'c1cccc(N(c2ccc(cc2)c2nc(C#N)c(nc2c2ccccc2)C#N)c2ccc(cc2)c2nc(C#N)c(nc2c2ccccc2)C#N)c1'
    m = Chem.MolFromSmiles(smi)
    #print(Chem.MolToMolBlock(m))
    mols.append(m)
    m3d = Chem.AddHs(m)
    AllChem.EmbedMolecule(m3d, randomSeed=1)
    #Draw.MolToImage(m3d, size=(250, 250)).show()
    m3d_without_h = Chem.RemoveHs(m3d)
    mols.append(m3d_without_h)
    bonds = m3d.GetBonds()
    single_bonds_id = []

    # find all single bonds without 'H' as end atom
    for bond in bonds:
        bond_type = bond.GetBondType()
        # print(bond_type)
        begin_atom = bond.GetBeginAtom()
        end_atom = bond.GetEndAtom()
        # print('begin atom: ' + begin_atom.GetSymbol())
        # print('end atom: ' + end_atom.GetSymbol())
        if str(bond_type) == 'SINGLE':
            if end_atom.GetSymbol() != 'H':
                single_bonds_id.append(bond.GetIdx())

    if len(single_bonds_id) == 0:
        print('no single bond, return')
        return
    frags = Chem.FragmentOnBonds(m, single_bonds_id)

    smis = Chem.MolToSmiles(frags)
    smis = smis.split('.')

    for smi in smis:
        print(smi)
        frag = Chem.MolFromSmiles(smi)
        # frag = Chem.AddHs(frag)
        # AllChem.EmbedMolecule(frag, randomSeed=1)
        # frag = Chem.RemoveHs(frag)
        mols.append(frag)
        patt = Chem.MolFromSmiles(smi)
        sub = m3d.GetSubstructMatch(patt)
        print(sub)


    img = Draw.MolsToGridImage(mols, molsPerRow=5, subImgSize=(400, 400), legends=['' for x in mols], options=opts)
    #img.show()


def get_atom_coordinate():
    smi = 'c1cccc(N(c2ccc(cc2)c2nc(C#N)c(nc2c2ccccc2)C#N)c2ccc(cc2)c2nc(C#N)c(nc2c2ccccc2)C#N)c1'
    m = Chem.MolFromSmiles(smi)
    m = Chem.MolToMolBlock(m)
    m = Chem.MolFromMolBlock(m)
    conf = m.GetConformer()
    patt = Chem.MolFromSmiles('C#N')
    sub = m.GetSubstructMatch(patt)

    for s in sub:
        print(m.GetAtoms()[s].GetSymbol(), list(conf.GetAtomPosition(s)))


if __name__ == '__main__':
    findsinglebond()
    # get_atom_coordinate()