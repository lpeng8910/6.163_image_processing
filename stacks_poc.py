from PIL import Image, ImageEnhance

PATH_TO_PARTITIONS = "../Mark_1_TIFF/"
PATH_TO_SAVE_IMAGES = "./stacks_poc_images/"
'''
param the number frame from each partition we want to stack
returns an image object of all the stacked frames
'''
def stack_images(frame): 
    frame = str(frame).zfill(3)
    prev_layer = Image.open(PATH_TO_PARTITIONS+ "partition1_tiff/partition1.avi00000"+ frame + ".tif")
    for partition in range(2,17): 
        im = Image.open(PATH_TO_PARTITIONS+ "partition"+str(partition)+"_tiff/partition"+str(partition)+".avi00000"+ frame + ".tif")
        #equation used in blend: image1 * (1.0 - alpha) + image2 * alpha
        new_layer = Image.blend(im,prev_layer,(partition-1)/partition)
        prev_layer = new_layer
        #uncomment for debugging
        #print("i'm on partition: " + str(partition))
    prev_layer.save(PATH_TO_SAVE_IMAGES + "stacked_frame"+frame+".tif")
    return PATH_TO_SAVE_IMAGES + "stacked_frame" + frame + ".tif"

'''
params 
    initial_image: string, name of initial image we're boosting
    final_image: string, name of final image we're boosting
    num: float, the amount to boost the image by. 0 gives black mage, 1.0 gives original image.
'''
def boost_brightness(initial_image, final_image, num):
    im = Image.open(initial_image)
    enhancer = ImageEnhance.Brightness(im)
    enhanced_im = enhancer.enhance(num)
    enhanced_im.save(PATH_TO_SAVE_IMAGES+final_image+".tif")
 
'''
this is just an example that stacks all the frame 1's together, then boosts its brightness
'''
stacks_name = stack_images(1)
boost_brightness(stacks_name,"enhanced_stack",10.0)
boost_brightness(PATH_TO_PARTITIONS+"partition1_tiff/partition1.avi00000001.tif","enhanced_single_partition_1_frame_1",10.0)

        
    



    
