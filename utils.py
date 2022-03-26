import zipfile


def unzip():
    filename = "lesmis.zip"
    zip_file = zipfile.ZipFile(f"./data/{filename}")

    zip_file.extractall("./data/")

    zip_file.close()

    print("unzip done. : ", filename)


if __name__ == "__main__":
    unzip()