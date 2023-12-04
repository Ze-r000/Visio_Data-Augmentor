
import Augmentor
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Specify the path")

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the --path argument
if args.path:
    print("The specified path is:", args.path)
    p = Augmentor.Pipeline(r"c:\Users\AI\Desktop\My-Dataset\Leo Delen")
    p .zoom(probability=0.9, min_factor=0.8, max_factor=1.5)
    p.flip_top_bottom(probability=0.2)
    p.random_brightness(probability=0.3, min_factor=0.3, max_factor=1.2)
    p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=50)
    # p.black_and_white(probability=0.3, threshold=150)
    # p.random_erasing(probability=0.9, rectangle_area=0.6)
    # p.rotate_random_90(probability=0.9)
    p.gaussian_distortion(probability=1,grid_width=2, grid_height=10, magnitude=10, corner="ur", method="in", mex=0.5, mey=0.5, sdx=0.65, sdy=0.05)
    p.shear(probability=1, max_shear_left=10, max_shear_right=20)
    p.shear(probability=1, max_shear_left=25, max_shear_right=10)
    p.sample(100)
else:                                                                               
    print("No path specified")