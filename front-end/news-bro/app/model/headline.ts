import React from "react";
import { BulletPoint } from "./bulletpoint";

export interface Headline {
    id: number
    title: string
    bulletpoints: BulletPoint[]
}

export interface HeadlinesResponse {
    headlines: Headline[]
}
