// Filename - pages/about.jsx
import React from "react";
import { experimentalStyled as styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Card from "react-bootstrap/Card";
import Emily from "../images/Emily.png";
import Ben from "../images/Ben.png";
import Spencer from "../images/Spencer.png";
import Winston from "../images/Winston.png";
import logo from "../images/logo.png";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#546581',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
    maxWidth: 400,
    minHeight: 220,
  color: theme.palette.text.secondary,
}));

const team = [
    {
        id: 1,
        title: "Winston Panzer",
        image: Winston,
        content: "Team Lead",
    },
    {
        id: 2,
        title: "Ben Johnson",
        image: Ben,
        content: "Test Lead",
    },
    {
        id: 3,
        title: "Spencer Kress",
        image: Spencer,
        content: "Technical Writer",
    },
    {
        id: 4,
        title: "Emily Schoener",
        image: Emily,
        content: "Quality Lead",
    }
    ]
// About our group, the class
const About = () => {
    return (
        <div>
            <h1>About the Discrete Math Solver</h1>
            <h2>Created by Team 11 for CS 499-03</h2>
            <br/>
            <h2>Our Team:</h2>
            <Box sx={{flexGrow: 1}}>
                <Grid container spacing={1} columns={{xs: 2, sm: 10, md: 15}}>
                    {team.map((person, index) => (
                        <Grid item xs={2} sm={4} md={4} key={index}>
                            <Item>
                                <Card>
                                    <h2>{person.title}</h2>
                                    <img src={person.image} width={120} height={140}/>
                                    <span style={{fontSize: 14, fontWeight: 'bold'}}><p>{person.content}</p></span>
                                    <br/>
                                </Card>
                            </Item>
                        </Grid>
                    ))}
                </Grid>
            </Box>
        </div>
    );
};

export default About;
