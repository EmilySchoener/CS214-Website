// Filename - pages/unit1.jsx
import React from "react";
import { Link } from 'react-router-dom'
import { experimentalStyled as styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Card from "react-bootstrap/Card";
import ListGroup from 'react-bootstrap/ListGroup';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#546581',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
    maxWidth: 400,
    minHeight: 220,
  color: theme.palette.text.secondary,
}));

const sections = [
    {
        id: 1,
        title: "Section 1.1",
        content: "Well Formed Formulas",
        link: "/unit1/section1_1"
    },
    {
        id: 2,
        title: "Section 1.1",
        content: "Either, Neither",
        link: "/unit1/section1_either"
    },
    {
        id: 3,
        title: "Section 1.1",
        content: "Profs",
        link: "/unit1/section1_1"
    },
    {
        id: 4,
        title: "Section 1.2",
        content: "Propositional Logic",
        link: "/unit1/section1_2"
    }
]

const Unit1 = () => {
    return (
        <div>
            <h1>
                Chapter 1
            </h1>
            <h2>Sections</h2>
            <Box sx={{flexGrow: 1}}>
                <Grid container spacing={1} columns={{xs: 2, sm: 10, md: 15}}>
                    {sections.map((unit, index) => (
                        <Grid item xs={2} sm={4} md={4} key={index}>
                            <Item>
                                <Card>
                                    <h2>{unit.title}</h2>
                                    <span style={{fontSize: 14, fontWeight: 'bold'}}><p>{unit.content}</p></span>
                                    <br/>
                                    <p>Add descriptor or example image.</p>
                                </Card>
                                <a href={unit.link}>
                                    <button> Go To {unit.title} </button>
                                </a>
                            </Item>
                        </Grid>
                    ))}
                </Grid>
            </Box>
        </div>
    );
};

export default Unit1;