def triangle_area(a, h):
    return a * h /2


if __name__ == "__main__":
    base = float(input())
    height = float(input())
    area = triangle_area(base, height)
    print(f"{area:.12g}")