from scripts import dependent as dp
import argparse

def fr_t():
	p = argparse.ArgumentParser()
	p.add_argument("--x", nargs='+', type=int, required=True)
	p.add_argument("--y", nargs='+', type=int, required=True)
	a = p.parse_args()
	fo = dp.frame(a.x,a.y)
	print(fo)

if __name__ == "__main__":
    fr_t()


