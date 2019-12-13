<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
#nav {
    padding: 30px;
}
#nav a {
    font-weight: bold;
    color: #2c3e50;
}
#nav a.router-link-exact-active {
    color: #42b983;
}
.pageMenu{
    background-color: #3b4252;
}
.pageMenu h2, button{
    display: inline-block;
}
.pageMenu h2{
    color: white;
}
</style>
