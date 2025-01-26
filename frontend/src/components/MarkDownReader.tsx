import ReactMarkdown from 'react-markdown';


const MarkdownReader = ({ content }: { content: string }) => {

    return (
        <div className="markdown-body">
            <ReactMarkdown>{content}</ReactMarkdown>
        </div>
    );
};

export default MarkdownReader;