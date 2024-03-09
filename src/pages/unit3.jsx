// Filename - pages/unit3.jsx
import React, {useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";

const Unit3 = () => {
    //The Initial state is 1 for the number of cases.
    const getInitialState = () => {
    return "1";
    }

    //Variables
    const [cases, setCases] = useState(getInitialState);
    const [char, setChar] = useState("");
    const [bases, setBases] = useState("");
    const [relation, setRelation] = useState("");

    //For input changes
    const casesChange= (e) => {
        setCases(e.target.value);
    }
    const charChange= (e) => {
        setChar(e.target.value);
    }
    const basesChange= (e) => {
        setBases(e.target.value);
    }
    const relationChange= (e) => {
        setRelation(e.target.value);
    }

    //When user presses the submit button.
    const handleSubmit = (e) => {
        e.preventDefault(); //This will stop the handler from emptying the text box.
        alert (`Cases Chosen: ${cases}, Char Chosen: ${char}
                \nBases Chosen: ${bases}\n
                Relation: ${char}(n) = ${relation}`);
    }

    //What is on the webpage.
    return (
        <div>
            <h1>
                Section 3.1 webpage.
            </h1>
            <form onSubmit={handleSubmit}>
                How many base cases do you have?
                <select id="dropdown" value={cases} onChange={casesChange}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
                <br/>
                <label>What character are you using?
                    <input
                        onChange={charChange}
                        type="text"
                        value={char}
                        placeholder="Enter Here"
                    />
                </label>
                <br/>
                <label>
                    Enter each of your base cases with a space in between each:
                    <input
                        onChange={basesChange}
                        type="text"
                        value={bases}
                        placeholder="Enter Base Cases Here"
                    />
                </label>
                <br/>
                <p>Enter in the recurrence relation: </p>
                <label>
                    {char}(n) =
                    <input
                        onChange={relationChange}
                        type="text"
                        value={relation}
                        placeholder="Enter Relation Here"
                    />
                </label>
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>
        </div>
    );
};

export default Unit3;