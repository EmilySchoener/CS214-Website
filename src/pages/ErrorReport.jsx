// Filename - pages/ErrorReport.jsx
import React, {useEffect, useState} from "react";
import axios from "axios";
import emailjs from '@emailjs/browser';

import {outPath} from '../Path.tsx';


const Report = () => {
    const path = outPath.path;

    const [formData, setFormData] = useState({
        from_name: '',
        email: '',
        section: '',
        input: '',
        output: '',
        message: '',
        userPath: path,
    });


    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        //console.log(history.location.pathname);
       emailjs.send("service_4ub3vtt","template_m34ykds",{
                    from_name: formData.from_name,
                    email: formData.email,
                    section: formData.section,
                    input: formData.input,
                    output: formData.output,
                    message: formData.message,
                    userPath: outPath.path}, {
        publicKey: 'TtHOty0oV0DN0RUEr',
      })
      .then(
        () => {
          alert('Email Sent!');
          //Dump Path stored after sending email.
          window.localStorage.setItem('PATH_STATE', " ");
        },
        (error) => {
          alert('Email failed to send.');
        },
      );
        try {
            const response = await axios.post('http://localhost:5000/submit', formData);
            console.log('Response from server:', response.data);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <h1>User Input</h1>
            <h2>Want to report an error or share input?</h2>
            <br/>
            <h2>Fill out this form:</h2>

            <form onSubmit={handleSubmit}>
                <label>Name:
                    <input type="text" name="from_name" value={formData.from_name} onChange={handleChange}/> </label>
                <br/>
                <label>Email:
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required/></label>
                <br/>
                <br/>
                <label>Section where error was identified:
                    <input type="text" name="section" value={formData.section} onChange={handleChange}
                           required/></label>
                <br/>
                <label>Your input:
                    <input type="text" name="input" value={formData.input} onChange={handleChange} required/></label>
                <br/>
                <label>The solution given:
                    <input type="text" name="output" value={formData.output} onChange={handleChange} required/></label>
                <br/>
                <p>Message:</p>
                <textarea name="message" cols={35} rows={10} value={formData.message}
                          onChange={handleChange}/><br/>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default Report;