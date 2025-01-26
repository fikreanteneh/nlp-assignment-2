import ThemeSwitcher from './components/ThemeSwitcher';
import Particles from './components/ui/particles';
import Home from './Home/Home';
import { ThemeProvider } from './ThemeProvider';


const Layout = () => {
  return (
    <div className="flex items-center justify-center min-h-screen bg-card" >
      {/* <DotPattern
        className={cn(
          "dot-pattern-mask"
          // "[mask-image:radial-gradient(600px_circle_at_center,white,transparent)]",
        )}
      /> */}
      <Particles
        className="absolute inset-0 z-0"
        quantity={200}
        ease={80}
        color={"#A07CFE"} //TODO: With Variable
        refresh
      />
      {/* <div className='z-[1]'>
                <Ripple />
            </div> */}
      <div className='z-[2]'>
        {/* <ShineBorder color={["#A07CFE", "#FE8FB5", "#FFBE7B"]}> */}
        <Home />
        {/* </ShineBorder> */}
      </div>
    </div>
  )
}

function App() {
  return (
    <ThemeProvider >
      <ThemeSwitcher />
      <Layout />
    </ThemeProvider>
  )
}

export default App
