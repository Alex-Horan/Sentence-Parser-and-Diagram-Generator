import React from "react";
import { useState } from "react";
import conImg from "../../../assets/images/conTree.png";
import depImg from "../../../assets/images/depTree.png"; 




//Parent component for entire app, safest and simplest way to replicate app state while still maintaining clean and readable code
export default function Display() {
    const [treeType, setTreeType] = useState("con"); //stores the selected type of graph
    const [typeSet, setType] = useState(true); //used to prevent an image from displaying before a sentence is submitted 
    const [firstOpen, endFirst] = useState(1);

    function httpRequest(sentence) {
        if (!typeSet) {
            setType(true);
        }
        return new Promise(() => {
            fetch("http://127.0.0.1:5000", {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(sentence)
            })

        // let imgRequest = await new fetch("http://localhost:5000/", {
        //     method: 'POST',
        //     headers: {"Content-Type": "application/json"},
        //     body: JSON.stringify(sentence)
        // }).then((response) => {
        //     response.text().then((responseString) => {
        //         alert(responseString);
        //         return "image displayed";
        //     })
        // }, () => {
        //     alert("onrejected response");
        // }).catch((e) => {setTimeout(() => {
        //     alert("help2");
        // }, 10)});
    })
    }



    function Form() {

        

        //will be where the http request to flask server is sent
        function handleFormSubmit(){
            if (firstOpen === 1) {
                endFirst(firstOpen - 1);
            }
            setType(true);
            let value = document.getElementById("sentence").value;
            // alert("text value is: " + value + ", radio button value is: " + treeType + ", and the typeset is equal to: " + typeSet);
            httpRequest(value); 
        }

        //input handler for radio buttons
        function handleRadioChange(e){
            setTreeType(e.target.value);
        }
        
        // actual html form that renders on screen
        return (
            <div>
                <form className="form" name='sentenceForm' onSubmit={handleFormSubmit}>
                    <input type="text" name="sentence" id="sentence" required="true" onChange={alert("change: " + typeSet)}></input>
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
                    <img className="graph" key={typeSet} src={conImg}/>
                )

            } else {

                return (
                    <img className="graph" key={typeSet} src={depImg}/>
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
    if (firstOpen === 1) {
        return (
            <div>
                <Form />
            </div>
        )
    } else {
        return(
            <div>
                <Image />
                <Form />
            </div>
        )
    }
}