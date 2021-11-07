import React, { useState } from "react";
import "../styles.css";

export default function NewListPopUp(props) {

    let [listName, setListName] = useState("");

    let handleClick = () => {
        props.toggle();
    };
    let handleSubmit = () => {
        props.toggle();
        props.createNewList(listName);
    }
    let handleOnChange = (event) => {
        setListName(event.target.value);
    }


    return (
        <div className="modal">
            <div className="modal_content">
            <span onClick={handleClick}>&times; </span>
            <p>Enter List Name</p>
            <input onChange={handleOnChange}></input>
            <button onClick={handleSubmit}>Create List</button>
            </div>
        </div>
    );
}