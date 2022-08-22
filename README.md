<div id="header" align="center">
<img src="https://user-images.githubusercontent.com/49791407/186008559-3df1f30c-fd2b-43e9-9b5a-d1902cfdab36.png">
<b>A 3d function grapher that allows for rotation and scaling of various mathematical functions</b>
</div>
<br>

![](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=blue&color=white) 
![](https://img.shields.io/tokei/lines/github/AJM432/3d-Function-Grapher) 
![](https://img.shields.io/github/repo-size/AJM432/3d-Function-Grapher?style=flat)

## Demo

<div align="center">
<img src="https://user-images.githubusercontent.com/49791407/186030712-4ba4775f-4b59-47c7-95b1-95e64ac51b4b.gif">
</div>

## Usage
- Use the (&#8593; &#8594; &#8595; &#8592; q w) keys to rotate the function in three dimensions.
- Press "r" to reset the view
- Use the (+ -) keys to zoom in and out of the function

## More Examples
<div id="examples" align="center">
<img src="https://user-images.githubusercontent.com/49791407/186031630-b51b2ae4-22df-48a0-9b06-e74550708751.png" width=32%>
<img src="https://user-images.githubusercontent.com/49791407/186031632-dfef870c-ecc1-4fb6-a07c-039e697c2f69.png" width=32%>
<img src="https://user-images.githubusercontent.com/49791407/186031633-eccb3b8a-8953-40b4-b56b-e666b7164db7.png" width=32%>
</div>

## Brief Overview of Program Mechanics
1. The program first computes and stores points in a three-dimensional Numpy matrix given a multidimensional function.
2. Next, when the user rotates the function, the program computes the dot product of the function matrix with a rotational matrix depending on the axis of rotation.
3. Then, the program computes the dot product of the function matrix with a projection matrix which converts the function matrix from 3d to 2d space.
4. Lastly, the resulting 2d matrix is blit to the screen by drawing triangles connecting adjoining points. 

## License
3d-Function-Grapher is licensed under the ![MIT License](https://github.com/AJM432/3d-Function-Grapher/blob/main/LICENSE.md)