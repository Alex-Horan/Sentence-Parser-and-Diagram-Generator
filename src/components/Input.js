import React from "react";
import { useState } from "react";
import { NoImage, Image } from "./Image";
import httpRequest from "../httpRequests";



function Input() {
    const [treeType, setType] = useState("con");
    const [tree, setTree] = useState("default");

    function getImageUrl() {
        if (tree === "default") {
            return (
                <NoImage/>
            )
        } else {
            return (
            <div>
                <Image treeType={tree}></Image>
            </div>
            )
        }
        
    }
    function handleRadioChange(e) {
        setType(e.target.value)
    }

    function handleFormSubmit(){
        let value = handleTextSubmit();
        alert("text value: " + value + ", radio value: " + treeType);
        alert(tree);
        setTree(treeType);
        alert(tree);
        httpRequest("http://localhost:5000", value)

    }

    function handleTextSubmit() {
        let textInp = document.getElementById("sentence");
        let value = textInp.value;
        return value;
    }

    return (
        <div>
         <form name='sentenceForm' onSubmit={handleFormSubmit}>
            <input type="text" name="sentence" id="sentence"></input>
            <label><input type="radio" name="tree" value="con" onChange={handleRadioChange} checked={treeType === "con"}></input>Constituents</label>
            <label><input type="radio" name="tree" value="dep" onChange={handleRadioChange} checked={treeType === "dep"}></input>Dependencies</label>
         </form>
         </div>       
    )
}



export default Input