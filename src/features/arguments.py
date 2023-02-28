from argparse import ArgumentParser, Namespace
def getArgspace():
    parser = ArgumentParser(
    prog = 'Extract Feature Vector for Image'
    usage = 'This module will allow you to extract feature vectors from images using a CNN of your choice.'
    )
    parser.add_argument(
            "-i",
            "--image-directory-path",
            help="Argument to specify input directory for preprocessed images",
            required=True,
            default=None
            )
    parser.add_argument(
            "-o", 
            "--ouput-directory-path",
            help="Arugment to specify ouput directory for extracted feature vectors",
            required=True,
            default='/output'
                                                                        )
    parser.add_argument(
            "-c",
            "--CNN-architecture-name",
            help="Specify the CNN architecture of choice (supported ones include: MobileNet, AlexNet, etc..."),
            required=True,
            default='MobileNet'
            )
    parser.add_argument(
            "-w",
            "--weights",
            help="Name of dataset the model has been trained on (imagenet, etc...)",
            default='imagenet'
            )
    return parser.parse_args()
