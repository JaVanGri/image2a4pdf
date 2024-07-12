from fpdf import FPDF
from tqdm import tqdm
from PIL import Image

def images_to_pdf(image_list, output_path):
    pdf = FPDF()
    a4_width_mm = 210
    a4_height_mm = 297

    for image_path in tqdm(image_list):
        with Image.open(image_path) as img:
            width_mm, height_mm = img.size[0] * 0.264583, img.size[1] * 0.264583
            scale = min(a4_width_mm / width_mm, a4_height_mm / height_mm)
            scaled_width = width_mm * scale
            scaled_height = height_mm * scale

            pdf.add_page()
            x_offset = (a4_width_mm - scaled_width) / 2
            y_offset = (a4_height_mm - scaled_height) / 2
            pdf.image(image_path, x_offset, y_offset, scaled_width, scaled_height)

    pdf.output(output_path, "F")

def list_images_in_dir(directory):

    import os

    image_extensions = ["jpg", "jpeg", "png", "gif", "bmp"]
    images = []
    for file in os.listdir(directory):
        if file.split(".")[-1].lower() in image_extensions:
            images.append(os.path.join(directory, file))

    images.sort()
    return images

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Convert a list of images to a PDF file.")
    parser.add_argument("directory", help="The directory containing the images.")

    parser.add_argument("--output", help="The output PDF file.", default=None)
    args = parser.parse_args()

    if args.output is None:
        args.output = args.directory + "result.pdf"

    images = list_images_in_dir(args.directory)
    images_to_pdf(images, args.output)

if __name__ == "__main__":
    main()