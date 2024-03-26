// Filename - pages/section5_2.jsx
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
        title: "Pert Chart",
        content: "Add example here",
        link: "/unit5/section5_2/PertChart"
    },
    {
        id: 2,
        title: "Closure Relations",
        content: "Add example here",
        link: "/unit5/section5_2/TopologicalSort"
    },
    {
        id: 3,
        title: "Sequential Tasks",
        content: "Add example here",
        link: "/unit5/section5_2/SequentialTasks"
    }
    ]
const Section5_2 = () => {
    return (
        <div>
            <h1>
                Section 5.2
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

export default Section5_2;