// Filename - pages/section5_1.jsx
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
        title: "Binary Relations",
        content: "Exercises 11 and 12",
        link: "/unit5/section5_1/BinaryRelations"
    },
    {
        id: 2,
        title: "Closure Relations",
        content: "Problems 23 and 24",
        link: "/unit5/section5_1/ClosureRelations"
    },
    /*{
        id: 3,
        title: "Hasse Diagram",
        content: "Problem 31",
        link: "/unit5/section5_1/HasseDiagram"
    },*/
    {
        id: 4,
        title: "Minimal, Maximal, Least, Greatest Elements",
        content: "Problem 32",
        link: "/unit5/section5_1/MMLGElements"
    },
    {
        id: 5,
        title: "Equivalence",
        content: "Problem 51",
        link: "/unit5/section5_1/Equivalence"
    }
    ]

const Section5_1 = () => {
     return (
        <div>
            <h1>
                Section 5.1
            </h1>
            <h2>Problems</h2>
            <Box sx={{flexGrow: 1}}>
                <Grid container spacing={1} columns={{xs: 2, sm: 10, md: 15}}>
                    {sections.map((unit, index) => (
                        <Grid item xs={2} sm={4} md={4} key={index}>
                            <Item>
                                <Card>
                                    <h2>{unit.title}</h2>
                                    <p>{unit.content}</p>
                                    <br/>
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

export default Section5_1;