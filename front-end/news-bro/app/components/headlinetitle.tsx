import React from 'react';
import Link from 'next/link';

interface PageTitleProps {
    title: string;
}

const PageTitle: React.FC<PageTitleProps> = ({ title }) => {
    return (
        <div className="flex items-baseline mb-40">
            <Link href="/">
                <div className="text-lg font-bold text-gray-500 hover:text-black focus:outline-none">
                    {'< Back'}
                </div>
            </Link>
            <h1 className="text-4xl font-bold text-black ml-4">{title}</h1>
        </div>
    );
};

export default PageTitle;
