'use client'
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import { Headline } from '@/app/model/headline';
import PageTitle from '@/app/components/headlinetitle';
import BulletPointComponent from '@/app/components/bulletpoint';
import Image from 'next/image'


export default function HeadlineComponent({ params }: { params: { id: string } }) {
    // Fetch news data based on the id parameter
    const [response, setResponse] = useState({} as Headline)

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/headline/${params.id}`,
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



    const headline: Headline = response

    const BulletPoints = () => {
        if (Object.keys(response).length === 0) {
            return (
                <h2>🌀 Loading...</h2>
            );
        }
        return (
            <div className="mb-32 grid text-center lg:max-w-5xl lg:w-full lg:mb-0 lg:grid-cols-4 lg:text-left">
                {response.bulletpoints.map((item, index) => (
                    <BulletPointComponent bulletPoint={item} />
                ))}
            </div>
        );
    }

    return (
        <main className="flex min-h-screen flex-col items-start p-24 font-mono">
            <PageTitle title={headline.title} />
            <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex lg: flex-col">                
                <BulletPoints />
            </div>
        </main>
    );
};
