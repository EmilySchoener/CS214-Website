// Filename - pages/5_1pages/BinaryRelations.jsx
import React, {useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";


const BinaryRelations = () => {
    const [text, setText] = useState("");
    const handleInputChange = (e) => {
        setText(e.target.value);
        console.log('inputChanged')
    }

    //When user presses the submit button.
    const handleSubmit = (e) => {
        e.preventDefault(); //This will stop the handler from emptying the text box.
        alert (`Text: ${text}`);
    }
    return (
        <div>
            <h1>
                5.1 - Binary Relations webpage.
            </h1>
            <p> Input: </p>
            <form onSubmit={handleSubmit}>
                <textarea
                    rows={5}
                    cols={35}
                    onChange={handleInputChange}
                    placeholder="Enter your problem"
                />
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>
            <p>
                Hello, {text}
            </p>
        </div>
    );
};

export default BinaryRelations