import React from "react";
import conImg from "../../resources/images/conTree.png";
import depImg from "../../resources/images/depTree.png";

export function NoImage() {
    return (
        <div></div>
    )
}


export function ConImage() {
    const url = `http://localhost:5000/static/testImage.png`;
    return (
        <div>
            <img src={conImg}/>
        </div>
    )
}

export function DepImage() {
    return (
        <div>
            <img src={depImg} />
        </div>
    )
}