# Context
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Imports
import Augmentor
from Augmentor.Operations import Operation
import tempfile
from PIL import Image
import io


# Custom class for testing
class DoubleImageSize(Operation):
    def __init__(self, probability, custom_parameter_integer):
        Operation.__init__(self, probability)
        self.custom_parameter_integer = custom_parameter_integer

    def do(self):
        for image in self.images:
            pass

    def perform_operation(self, images):
        for i in range(self.custom_parameter_integer):
            pass

        for image in images:
            image = image.resize((image.size[0]*2, image.size[1]*2))

        return images


def test_adding_custom_function():
    width = 80
    height = 80

    tmpdir = tempfile.mkdtemp()
    tmps = []

    for i in range(10):
        tmps.append(tempfile.NamedTemporaryFile(dir=tmpdir, suffix='.JPEG', delete=False))

        bytestream = io.BytesIO()

        im = Image.new('RGB', (width, height))
        im.save(bytestream, 'JPEG')

        tmps[i].file.write(bytestream.getvalue())
        tmps[i].flush()

    p = Augmentor.Pipeline(tmpdir)

    assert len(p.augmentor_images) == len(tmps)

    # Use the DoubleImageSize custom operation above
    #
    # First instantiate a new object of the custom operation
    double_image_size_operation = DoubleImageSize(probability=1, custom_parameter_integer=5)

    # Add to pipeline
    p.add_operation(double_image_size_operation)

    # Executed the pipeline as normal, and your custom operation will be executed
    p.sample(10)


def test_execute_custom_function():
    pass
