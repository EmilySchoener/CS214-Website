import React from "react";
import Navbar from "./Navbar/index.jsx";
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import logo from "./images/logo.png";

//These are the webpages available.
import Home from './pages/index.jsx';
import About from './pages/about.jsx';
import Unit1 from "./pages/unit1.jsx";
import Section1_1 from "./pages/section1.jsx";
import Section1_2 from "./pages/section1_2.jsx";
import Unit3 from "./pages/unit3.jsx";
import Unit4 from "./pages/unit4.jsx";
import Unit5 from "./pages/unit5.jsx";
import Section5_1 from "./pages/section5_1.jsx";
import Section5_2 from "./pages/section5_2.jsx";
import Section5_4 from "./pages/section5_4.jsx";
import Section5_5 from "./pages/section5_5.jsx";
import Section5_7 from "./pages/section5_7.jsx";
import Unit6 from "./pages/unit6.jsx";
import Section6_1 from "./pages/section6_1.jsx";
import Section6_2 from "./pages/section6_2.jsx";
import Unit7 from "./pages/unit7.jsx";

//Router is for different paths on the navbar. Home is the homepage.
function App() {
    return (
        <div>
    <Router>
        <Navbar>
        </Navbar>
        <Routes>
        <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/unit1" element={<Unit1 />} />
                <Route path="/unit1/section1_1" element={<Section1_1 />} />
                <Route path="/unit1/section1_2" element={<Section1_2 />} />
                <Route path="/unit3" element={<Unit3 />} />
                <Route path="/unit4" element={<Unit4 />} />
                <Route path="/unit5" element={<Unit5 />} />
                <Route path="/unit5/section5_1" element={<Section5_1 />} />
                <Route path="/unit5/section5_2" element={<Section5_2 />} />
                <Route path="/unit5/section5_4" element={<Section5_4 />} />
                <Route path="/unit5/section5_5" element={<Section5_5 />} />
                <Route path="/unit5/section5_7" element={<Section5_7 />} />
                <Route path="/unit6" element={<Unit6 />} />
                <Route path="/unit6/section6_1" element={<Section6_1 />} />
                <Route path="/unit6/section6_2" element={<Section6_2 />} />
                <Route path="/unit7" element={<Unit7 />} />
            </Routes>
        </Router>
        </div>
    );
}

export default App;
