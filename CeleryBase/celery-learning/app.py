from tasks import add


if __name__ == "__main__":
    print("Start task...")
    # result = add.apply_async(4, 6)
    result = add.delay(4, 6)    # 提交任务
    print("End...")
    print(result)