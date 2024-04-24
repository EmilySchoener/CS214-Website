// Filename - pages/5_4pages/Onto.jsx
import React, {useEffect, useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';


const Onto = () => {

    const [domain, setDomain] = useState("");
    const [codomain, setCoDomain] = useState("");
    const [func, setFunc] = useState("");
    const [responseData, setResponseData] = useState(null);
    console.log(responseData);
    //When user presses the submit button.
       const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
           // alert (`Domain ${domain}, CoDomain: ${codomain}, Function: ${func}`);
            const response = await axios.post("http://127.0.0.1:5000/submitOnto", {
                domain,
                codomain,
                func,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }

    }

    const DomainChange= (e) => {
        setDomain(e.target.value);
    }

     const CoDomainChange= (e) => {
        setCoDomain(e.target.value);
    }

     const funcChange= (e) => {
        setFunc(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/submitOnto")
      .then(response => {
        // Update the state with the response data
        setResponseData(response.data);
      })
      .catch(error => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
    }

    useEffect(() => fetchData(), []);

       console.log(responseData);
    return (
        <div>
            <h1>
                5.4 - Onto webpage.
            </h1>
            <Splitter>
                <SplitterPanel>
            <p> Input: </p>
            <form onSubmit={handleSubmit}>
                <label> Type in the Domain:
                    <input
                        onChange={DomainChange}
                        placeholder="Enter the domain"
                    />
                </label>
                <br/>
                <label> Type in the Co-Domain:
                    <input
                        onChange={CoDomainChange}
                        placeholder="Enter the codomain"
                    />
                </label>
                <br/>
                <label> Type in the set of the function:
                    <input
                        onChange={funcChange}
                        placeholder="Enter the set of the function"
                    />
                </label>
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>
            <h2>Solution</h2>
                    {responseData}

             </SplitterPanel>
                <SplitterPanel>
                    <h2>Example:</h2>
                    <p>Type in the Domain: [1,2,3,4]  </p>
                    <p>Type in the Co-Domain: [1,2,3,4,5]  </p>
                    <p> Type in the Function: [[1,2],[3,4],[5,7]]</p>
                    <p>Output: The function is not Onto <br/>
                        </p>
                </SplitterPanel>
            </Splitter>
        </div>
    );


};

export default Onto