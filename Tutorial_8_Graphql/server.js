const { authors, books } = require("./simpledata"); // Data

const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const {
	GraphQLSchema,
	GraphQLObjectType,
	GraphQLString,
	GraphQLList,
	GraphQLInt,
	GraphQLNonNull
} = require("graphql");


const app = express();

const BookType = new GraphQLObjectType({
	name: "Book",
	description: "Este es un libro escrito por un autor",
	fields: () => ({
		id: { type: GraphQLNonNull(GraphQLInt) },
		name: { type: GraphQLNonNull(GraphQLString) },
		authorId: { type: GraphQLNonNull(GraphQLString) },
		// Aqui se crea un campo que se consigue de AuthorType
		author: { 
			type: AuthorType,
			resolve: (book) => {
				return authors.find(author => author.id === book.authorId)
			}
		}
	})
})

const AuthorType = new GraphQLObjectType({
	name: "Author",
	description: "Esto representa un autor de un libro",
	fields: () => ({
		id: { type: GraphQLNonNull(GraphQLInt) },
		name: { type: GraphQLNonNull(GraphQLString) },
		books: {
			type: new GraphQLList(BookType),
			resolve: (author) => {
				return books.filter(book => book.authorId === author.id)
			}
		},
	})
})

const RootQueryType = new GraphQLObjectType({
	name: "Query",
	description: "Root query",
	fields: () => ({
		book: {
			type: BookType,
			description: "Lista solo un libro",
			args: {
				id: { type: GraphQLInt }
			},
			resolve: (parent, args) => books.find(book => book.id === args.id)
		},
		books: {
			type: new GraphQLList(BookType),
			description: "Lista de todos los libros",
			resolve: () => books
		},
		author: {
			type: AuthorType,
			description: "Lista solo un autor",
			args: {
				id: { type: GraphQLInt }
			},
			resolve: (parent, args) => authors.find(author => author.id === args.id)
		},
		authors: {
			type: new GraphQLList(AuthorType),
			description: "Lista todos los autores",
			resolve: () => authors
		}
	})
})

// Similar a un post, aquí se crean nuevos datos
const RootMutationType = new GraphQLObjectType({
	name: "Mutation",
	description: "Root Mutation, para modificar",
	fields: () => ({
		addBook: {
			type: BookType,
			description: "Crear un libro",
			args: {
				name: { type: GraphQLNonNull(GraphQLString) },
				authorId: { type: GraphQLNonNull(GraphQLInt) }
			},
			resolve: (parent, args) => {
				const book = {
					id: books.length + 1,
					name: args.name,
					authorId: args.authorId
				};
				books.push(book);
				return book;
			}
		},
		addAuthor: {
			type: AuthorType,
			description: "Crear un autor",
			args: {
				name: { type: GraphQLNonNull(GraphQLString) }
			},
			resolve: (parent, args) => {
				const author = {
					id: authors.length + 1,
					name: args.name
				};
				authors.push(author);
				return author;
			}
		}
	})
})

const schema = new GraphQLSchema({
	query: RootQueryType,
	mutation: RootMutationType
})

app.use("/graphql", graphqlHTTP({
	schema: schema,
	graphiql: true
}));

app.listen(5000, () =>{
	console.log(" [Server] Running on port 5000")
});