# ARLab

This respository serves to purpose to display some of the work that was completed in my reserch lab while studying abroad.
The end result is being able to recreate a 3D environment by using IOS logger. Then that recreation can then be plugged into Unity to create an interactable environment.

## Steps used to create the 3D environment:
1) Download [IOS_logger](https://github.com/Varvrar/ios_logger) onto phone.
2) Take video of surrounding area making sure to get around objects and multiple angles for max precision.
3) Upload video and gyroscopic data into NTU's python script to convert the video into a mesh and the gyroscopic data into camera transformations: [ARPoses.txt](https://github.com/jwbarkes/ARLab/blob/main/IOSVideoData/ARposes.txt).
4) Open the mesh in MeshLab and make adjustments if necessary.
5) Bring the mesh into Unity and add a rigidbody to the obj.
6) Create a script and add it to the scene which creates a game object when a solid surface is clicked on.
7) Create a script and add it to the camera which takes the camera transformations and applies them to the scene camera (Only do this step if you want an interactive video, otherwise you can skip this to just have an interactable scene of your environment).
8) Run the scene and enjoy an interactable video/scene.
