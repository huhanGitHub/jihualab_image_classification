import os

file_dir = r'E:\Verify'
suffix = '.out'
result_path = os.path.join(file_dir, 'all_results.txt')


def first_TripletA_SingletA(file_path, result_path):
    files = {}
    with open(file_path) as f:
        for line in f.readlines():
            if line == '':
                continue
            words = line.split(' ')
            file = words[0]
            file_list = files.get(file)
            if file_list is None:
                files[file] = [line]
            else:
                file_list.append(line)
                files[file] = file_list

    results = []
    for key in files.keys():
        file_list = files.get(key)
        triplet_status = False
        singlet_status = False
        for line in file_list:
            if not triplet_status and 'Triplet-A' in line:
                triplet_status = True
                results.append(line)
            if not singlet_status and 'Singlet-A' in line:
                singlet_status = True
                results.append(line)

            if triplet_status and singlet_status:
                break

    with open(result_path, 'a+', encoding='utf8') as f:
        for line in results:
            f.write(line)


def traverse_first_TripletA_SingletA(file_dir, suffix, result_path='.all_results.txt'):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if str(file).endswith(suffix):
                file_path = os.path.join(root, file)
                first_TripletA_SingletA(file_path, result_path)


if __name__ == '__main__':
    traverse_first_TripletA_SingletA(file_dir, suffix, result_path)
