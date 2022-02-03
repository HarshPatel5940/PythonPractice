function HelloWorld(): string {
    console.log("Functions we love them!!\t");
    return "Hello World...";
}

const x1 = HelloWorld;

const x2 = HelloWorld();

console.log(x1, x2);
