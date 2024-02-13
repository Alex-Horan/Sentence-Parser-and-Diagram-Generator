import React from "react";
import { useState } from "react";




function Input() {
    const [treeType, setType] = useState("con");

    function handleRadioChange(e) {
        setType(e.target.value)
    }

    function handleFormSubmit(){
        let value = handleTextSubmit();
        alert("text value: " + value + ", radio value: " + treeType);
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