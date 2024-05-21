from tqdm import tqdm

# 生成所有可能的手机号码
def generate_all_phone_numbers():
    prefixes = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139'] #号段自己添加
    for prefix in tqdm(prefixes, desc="Generating phone numbers"):
        phone_numbers = []
        for i in range(100000000):
            phone_number = prefix + str(i).zfill(8)  # 使用zfill填充后八位为固定长度
            phone_numbers.append(phone_number)
        save_phone_numbers_to_file(prefix, phone_numbers)

# 保存手机号码到文件
def save_phone_numbers_to_file(prefix, phone_numbers):
    filename = prefix + "_phone_numbers.txt"
    with open(filename, 'w') as file:
        for phone_number in phone_numbers:
            file.write(phone_number + '\n')

# 主函数
def main():
    generate_all_phone_numbers()
    print("所有手机号码生成完成！")

if __name__ == "__main__":
    main()
