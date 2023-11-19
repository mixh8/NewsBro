'use client';
import { useEffect, useState } from "react";
import React from "react";
import { Headline, HeadlinesResponse } from "../model/headline";
import Link from "next/link";


export function Headlines() {
    const [response, setResponse] = useState({} as HeadlinesResponse)

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api',
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Origin': 'http://localhost:3000',
                },
            }
        )
            .then(res => res.json())
            .then(data => {
                setResponse(data)
            })
    }, [])

    if (Object.keys(response).length === 0) {
        return (
            <h2>🌀 Loading...</h2>
        );
    }

    const headlines: Headline[] = response.headlines
    return (
        headlines.map((headline) => (
            <a
                href={`/headlines/${headline.id}`}
                className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30"
                rel="noopener noreferrer"
            >
                <h2 className={`mb-3 text-2xl font-semibold`}>
                    {headline.title}{' '}
                    <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
                        -&gt;
                    </span>
                </h2>
                <p className={`m-0 max-w-[30ch] text-sm opacity-50 font-mono`}>
                    {/* Find in-depth information about Next.js features and API. */}
                </p>
            </a>
        ))


    )
}