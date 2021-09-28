# @ Code - Blocks

## How to contribute ?
1. Fork / Clone this repo into your github account.
2. Paste your project inside ` /projects/<project_name> `folder.
3. Also put your **photo inside this same folder** , so you can use it on card.
4. Create a card for your project inside `/projects.html. `

## How to create the card
>Use the given below code snippet to create the card
```
<div class="card bg-light shadow">
                <div class="card-left bg-red-dark">
                    <div class="card-contributer-picture">
                <!-- Change below here -->
                        <img src="  projects/<folder name>/<photo.jpg> " alt=" <Your Name> ">
            
                    </div>
                    <div class="card-contributer-name">

                <!-- Change below here -->
                        <a class="mont-semi-bold-italic txt-white hover-underline-animation" href="https://www.github.com/ <your github id>"> <your name> </a>
            
                    </div>
                </div>
                <div class="card-right bg-dark">
                    <div class="card-header mont-bold txt-white">

                    <!-- Change below here -->
                        <a href="projects/<project folder name>">
                        <h4 class="hover-underline-animation"> <project name> </h4>
                        </a>

                        <hr>

                        <p class="mont-light "> 
                                <!-- Add your project's description -->
                                <project description>

                        </p>

                    </div>
                    <div class="card-footer mont-light">

                   <!-- Change below Here (Tags) --> 
                        <p class="bg-red-dark txt-white">html</p>
                        <p class="bg-red-dark txt-white">css</p>

                    </div>
                </div>
            </div>
```
> You have to change at 7 places + the tags.