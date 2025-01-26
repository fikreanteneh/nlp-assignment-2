import useTheme from '../ThemeProvider';

const ThemeSwitcher = () => {
    const { currentTheme, changeTheme } = useTheme();

    const handleThemeChange = () => {
        changeTheme(currentTheme === 'dark' ? 'light' : 'dark');
    };


    return (
        <div className="fixed top-0 right-0 flex gap-4">
            <button onClick={handleThemeChange} className="p-2 bg-gray-200 rounded">
                Toggle Theme
            </button>
        </div>
    );
};

export default ThemeSwitcher;