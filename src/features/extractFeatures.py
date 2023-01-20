# import TF library with pretrained CNNs

# function for command line arguments using argparse
    # use argparse for this; maybe import a separate module

# function with arguments like what CNN wanting to use, preprocessed images directory, output feature directory
def featureExtraction(imageDirectoryPath, outputDirectoryPath, CNN = 'MobileNet', weights='imagenet'):
    '''
    Function: 
    - This function will convert images to feature vectors using a CNN architecture and weights of your choice.
    Required Arguments:
    - imageDirectoryPath = 'PATH TO PREPROCESSED IMAGES'
    - outputDirectoryPath = 'OUTPUT PATH'
    Optional Arguments:
    - CNN = 'NAME OF CNN'
        + The following are supported: 'MobileNet', 'ImageNet', ...
        + By default will use MobileNet
    - weights = 'NAME OF DATASET'
        + The following are supported: 'imagenet', ...
        + By default will use imagenet
    '''

print(featureExtraction.__doc__)
    # execute function to save feature vectors into the output directory as a TFRecords file
# if __name__ == '__main__':
#     print(featureExtraction.__doc__)
