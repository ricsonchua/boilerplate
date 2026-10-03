from . import basic as b
import argparse, json

def main():
	p = argparse.ArgumentParser()
	p.add_argument("--x", type=float, required=True)
	p.add_argument("--y", type=float, required=True)
	a = p.parse_args()
	o1 = b.addition(a.x,a.y)
	o2 = b.subtraction(a.x,a.y)
	print(json.dumps({"sum": float(o1), "sub": float(o2)}))


def ex():
	p = argparse.ArgumentParser()
	p.add_argument("--x", type=str, required=True)
	p.add_argument("--y", type=str, required=True)
	a = p.parse_args()
	print(json.dumps({"sum": str(a.x), "sub": str(a.y)}))

#Whatever is in the dunder will be executed with python -m 
if __name__ == "__main__":
    ex()

