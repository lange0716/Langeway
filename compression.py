import zlib, sys

file_in = "compressionFile.txt"
file_out = "compressedData.txt"

with open(file_in, mode="rb") as fin, open(file_out, mode="wb") as fout:
    data = fin.read()
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    print(f"Original size: {sys.getsizeof(data)}")
    # Original size: 42367 bytes
    print(f"Compressed size: {sys.getsizeof(compressed_data)}")
    # Compressed size: 227 bytes

    fout.write(compressed_data)

with open(file_out, mode="rb") as fin:
    data = fin.read()
    compressed_data = zlib.decompress(data)
    print(f"Compressed size: {sys.getsizeof(data)}")
    # Compressed size: 227 bytes
    print(f"Decompressed size: {sys.getsizeof(compressed_data)}")
    # Decompressed size: 42367 bytes