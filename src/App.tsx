import React from "react";
import Navbar from "./Navbar/index.jsx";
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";

//These are the webpages available.
import Home from './pages/index.jsx';
import About from './pages/about.jsx';
import Unit1 from "./pages/unit1.jsx";
import Section1_1 from "./pages/section1.jsx";
import Section1_2 from "./pages/section1_2.jsx";
import Unit3 from "./pages/unit3.jsx";
import Unit4 from "./pages/unit4.jsx";

//Router is for different paths on the navbar. Home is the homepage.
function App() {
    return (
        <div>
    <Router>
        <Navbar/>
        <Routes>
        <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/unit1" element={<Unit1 />} />
                <Route path="/unit1/section1_1" element={<Section1_1 />} />
                <Route path="/unit1/section1_2" element={<Section1_2 />} />
                <Route path="/unit3" element={<Unit3 />} />
                <Route path="/unit4" element={<Unit4 />} />
            </Routes>
        </Router>
        </div>
    );
}

export default App;
