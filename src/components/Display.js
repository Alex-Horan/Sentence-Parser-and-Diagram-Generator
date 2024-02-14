import React from "react";
import { useState } from "react";
import conImg from "../../resources/images/conTree.png";
import depImg from "../../resources/images/depTree.png"; 


//Parent component for entire app, safest and simplest way to replicate app state while still maintaining clean and readable code
export default function Display() {
    const [treeType, setTreeType] = useState("con"); //stores the selected type of graph
    const [typeSet, setType] = useState(false); //used to prevent an image from displaying before a sentence is submitted 

    function Form() {
        //will be where the http request to flask server is sent
        function handleFormSubmit(){
            setType(true);
            let value = document.getElementById("sentence").value;
            alert("text value is: " + value + ", radio button value is: " + treeType + ", and the typeset is equal to: " + typeSet);
        }

        //input handler for radio buttons
        function handleRadioChange(e){
            setTreeType(e.target.value);
        }

        // actual html form that renders on screen
        return (
            <div>
                <form className="form" name='sentenceForm' onSubmit={handleFormSubmit}>
                    <input type="text" name="sentence" id="sentence"></input>
                    <label><input type="radio" name="tree" value="con" onChange={handleRadioChange} checked={treeType === "con"}></input>Constituents</label>
                    <label><input type="radio" name="tree" value="dep" onChange={handleRadioChange} checked={treeType === "dep"}></input>Dependencies</label>
                </form>
            </div>     
        )
    }

    //component for the two types of trees
    function Image() {

        //determines whether to render dependency tree or constituent tree
        function ImageSet() {

            if (treeType === "con") {

                return (
                    <img className="graph" src={conImg}/>
                )

            } else {

                return (
                    <img className="graph" src={depImg}/>
                )
            }
        }

        return (
            <div>
                { 
                    typeSet ? (<ImageSet/>) : (<div></div>) //determines whether or not to render an image
                }
            </div>
        )
    }

    //final return for parent component
    return(
        <div>
            <Image />
            <Form />
        </div>
    )

}