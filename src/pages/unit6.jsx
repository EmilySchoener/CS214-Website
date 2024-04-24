// Filename - pages/unit6.jsx
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
    /*
    {
        id: 1,
        title: "Section 6.1",
        content: "Graphs and Their Representations",
        link: "/unit6/section6_1"
    },
    */
    {
        id: 2,
        title: "Section 6.2",
        content: "Trees and Their Representations",
        link: "/unit6/section6_2"
    }
    ]
const Unit6 = () => {
    return (
        <div>
            <h1>
                Chapter 6
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

export default Unit6;