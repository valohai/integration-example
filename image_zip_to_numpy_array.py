import argparse
import glob
import os
import zipfile

from PIL import Image
import numpy as np
import h5py


def get_zip_path(inputs_dir, input_name):
    search_expression = os.path.join(inputs_dir, input_name, '*.zip')
    zip_files = glob.glob(search_expression)
    assert len(zip_files) > 0, 'no zip files found with "{}"'.format(search_expression)
    assert len(zip_files) == 1, 'more than one zip found with "{}"'.format(search_expression)
    return zip_files[0]


def main(settings):
    zip_path = get_zip_path(settings.inputs_dir, 'my-datasets')

    rows = []

    with zipfile.ZipFile(zip_path, 'r') as zip:
        # infolist contains filename and filemode for each file inside the archive without extracting them
        # https://docs.python.org/3/library/zipfile.html#zipinfo-objects
        for info in zip.infolist():
            file_basename = os.path.basename(info.filename)

            # ignore hidden files, e.g. Mac OS metafile ("._...png")
            if file_basename.startswith('.'):
                continue

            # ignore non-PNG files
            if not file_basename.endswith('.png'):
                continue

            with zip.open(info.filename, 'r') as file_in_zip:
                img = Image.open(file_in_zip)

                # here we can do various kind of feature extraction; grayscaling, resizing, etc.
                # in this case, we are converting images to RGB to remove any potential transparency
                # from the images as well as resizing every image to the same size
                transformed_img = img.convert('RGB').resize((64, 64))

                # converting the image to a numpy array
                # we are dividing the numbers with 255 to map the original RGB colors that range from 0 to 255
                # to a normalized range from 0.0 to 1.0
                im = np.array(transformed_img) / 255.0

                # we print the name of the file, the shape of the numpy array
                # and the sum of color values for debugging
                print(file_basename, im.shape, im.sum())

                # the resulting arrays can also be converted back to images if required
                # result = Image.fromarray((im * 255).astype(np.uint8))
                # result.save(os.path.join(settings.outputs_dir, file_basename))

                rows.append(im)

    dataset = np.array(rows)
    print('dataset', dataset.shape)

    # you can save this dataset to e.g. a HDF5 file to be uploaded for further usage
    # all of this is of course totally optional and just a one way to manage your features
    h5f = h5py.File(os.path.join(settings.outputs_dir, 'features.h5'), 'w')
    h5f.create_dataset('dataset_1', data=dataset)
    h5f.close()


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs_dir', type=str, default=os.getenv('VH_INPUTS_DIR', './inputs'))
    parser.add_argument('--outputs_dir', type=str, default=os.getenv('VH_OUTPUTS_DIR', './outputs'))
    settings = parser.parse_args()
    main(settings)


if __name__ == "__main__":
    cli()
