import React from "react";

export const outPath = {
    path : "",
    pathChange : (e: string) => {
        outPath.path = outPath.path + " => "+ e;
        return outPath.path;
    },
    setPath : (e: string) => {
        outPath.path = e;
        return outPath.path;
    }
};
