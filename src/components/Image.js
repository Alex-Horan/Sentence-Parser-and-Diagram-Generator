import React from "react";

export function NoImage() {
    return (
        <div></div>
    )
}


export function Image() {
    const url = `http://localhost:5000/static/testImage.png`;
    return (
        <div>
            <img src="./testImage.png"/>
        </div>
    )
}