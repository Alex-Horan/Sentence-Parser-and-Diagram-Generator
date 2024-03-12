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
    
    //network request to the flask server
    async function httpRequest(sentence) {

        return await new Promise(() => {
            fetch("http://127.0.0.1:5000", {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(sentence)
            }).then(() => {
                //removes buffer circle after request finishes
                firstOpen.current = "no"; 
                $(".TreeType").prop("disabled", false);
                $(".TextEntry").prop("disabled", false);
                $(".graph").removeClass('loads');
                $("#spinner")
                    .removeClass('loading')
                        .addClass('loads');},
                 () => {
                    // firstOpen.current = "no"; 
                    // $(".TreeType").prop("disabled", false);
                    // $(".TextEntry").prop("disabled", false);
                    // $(".graph").removeClass('loads'); 
                    // $("#spinner")
                    //     .removeClass('loading')
                    //         .addClass('loads')
                    alert("Error 01: Network request has failed. Please ensure you are connected to the internet and the Flask server is running on port 5000");
                    throw new Error("Fetch rejected");
                })
        })
    }


    function Form() {
        //will be where the http request to flask server is sent
        function handleFormSubmit(e){
            //replaces image with loading circle
            $(".TreeType").prop("disabled", true);
            $(".TextEntry").prop("disabled", true);
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
                <form className="SentenceForm" name='sentenceForm' onSubmit={handleFormSubmit}>
                    <input type="text" name="sentence" className="TextEntry" id="sentence" required="true" placeholder="Enter a sentence..."></input>
                    <label className="TreeType"><input type="radio" name="tree" className="TreeType" value="dep" onChange={handleRadioChange} checked={treeType === "dep"}></input>Dependencies</label>
                    <label className="TreeType"><input type="radio" name="tree" className="TreeType" value="con" onChange={handleRadioChange} checked={treeType === "con"}></input>Constituents</label>
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
                    <div className="conDiv">
                    <img className="graph con" src={conImg}/>
                    <div id="spinner" className="loads" ></div>
                    </div>
                )

            } else {

                return (
                    <div className="depDiv">
                        <div className="img-wrapper">
                            <img className="graph" src={depImg}/>
                        </div>

                        <div id="spinner" className="loads" ></div>
                    </div>
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
            <div className="Start">
                <Form />
            </div>
        )
    }
    
}