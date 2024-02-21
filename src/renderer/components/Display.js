import React from "react";
import { useState } from "react";
import conImg from "../../../assets/images/conTree.png";
import depImg from "../../../assets/images/depTree.png"; 
import { useRef } from "react";
import $ from 'jquery';

//Parent component for entire app, safest and simplest way to replicate app state while still maintaining clean and readable code
export default function Display() {
    const firstOpen = useRef("yes");
    const [treeType, setTreeType] = useState("con"); //stores the selected type of graph
    
    
    function httpRequest(sentence) {

        return new Promise(() => {
            fetch("http://127.0.0.1:5000", {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(sentence)
            }).then(() => {firstOpen.current = "no"; $(".graph").removeClass('loads');$("#spinner").removeClass('loading').addClass('loads')}, () => {firstOpen.current = "no"; $(".graph").removeClass('loads'); $("#spinner").removeClass('loading').addClass('loads')})
        })
    }


    function Form() {
        //will be where the http request to flask server is sent
        function handleFormSubmit(e){
            $(".graph").addClass('loads');
            $("#spinner").addClass('loading').removeClass('loads')
            let value = document.getElementById("sentence").value;
            // alert("text value is: " + value + ", radio button value is: " + treeType + ", and the typeset is equal to: " + typeSet);
            httpRequest(value);
            e.preventDefault();
        }

        //input handler for radio buttons
        function handleRadioChange(e){
            setTreeType(e.target.value);
            // e.preventDefault();
        }
        
        // actual html form that renders on screen
        return (
            <div>
                <form className="form" name='sentenceForm' onSubmit={handleFormSubmit}>
                    <input type="text" name="sentence" id="sentence" required="true"></input>
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
                    <>
                    <img className="graph" src={conImg}/>
                    <div id="spinner" className="loads" ></div>
                    </>
                )

            } else {

                return (
                    <>
                    <img className="graph" src={depImg}/>
                    <div id="spinner" className="loads" ></div>
                    </>
                )
            }
        }

        return (
            <div>
                { 
                    (firstOpen.current === "no") ? (<ImageSet/>) : (<div></div>) //determines whether or not to render an image
                }
            </div>
        )
    }

    //final return for parent component
    if ((firstOpen.current) === "no") {
        return(
            <div>
                <Image />
                <Form />
            </div>
        )
    } else if (firstOpen.current === "yes") {
        return (
            <div>
                <Form />
            </div>
        )
    }
    
}