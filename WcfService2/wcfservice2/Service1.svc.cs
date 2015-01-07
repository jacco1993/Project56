using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Builders;
using MongoDB.Driver.GridFS;
using MongoDB.Driver.Linq;
using MongoDB;
using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson.IO;
using System.Web.Script.Serialization;
using Newtonsoft.Json;
using System.Diagnostics;
using System.IO;
using System.Text.RegularExpressions;


namespace WcfService2
{
    public class Products
    {
        public ObjectId _id { get; set; }
        public List<Beschrijving> beschrijving { get; set; }
        public List<Specs> specs { get; set; }
        public String price { get; set; }
        public String titles { get; set; }
        public String description { get; set; }
    }

    public class Prijs
    {
        public ObjectId _id { get; set; }
        public String titles { get; set; }
        //public String 123123123 { get; set; }
    }

    public class Specs 
    {
        public String name { get; set;}
        public String value { get; set; }
    }

    public class Beschrijving
    {
        public String name { get; set; }
        public String value { get; set; }
    }

    public class Service1 : IService1
    {
        public MongoDatabase connect(String databaseNaam)
        {
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            MongoDatabase database = server.GetDatabase(databaseNaam);
            return database;
        }

        public String[] collectionArray()
        {
            String[] collections = new String[12];
            collections[0] = "Behuizingen";
            collections[1] = "Controllers";
            collections[2] = "Energie";
            collections[3] = "Geluidskaarten";
            collections[4] = "Hardeschijf";
            collections[5] = "Koeling";
            collections[6] = "Moederborden";
            collections[7] = "Netwerk";
            collections[8] = "NetwerkOpslag";
            collections[9] = "OptischeDrivers";
            collections[10] = "Processoren";
            collections[11] = "Geheugen";
            return collections;
        }
        public List<Products> getAllProducts()
        {
            List<Products> total = new List<Products>();

            for (int x = 0;x < 12; x++)
            {
                String[] array = collectionArray();
                MongoCollection<Products> products = connect("Products").GetCollection<Products>(array[x]);
                MongoCursor<Products> allProducts = products.FindAll();
                List<Products> productsList = allProducts.ToList();
                total.AddRange(productsList);
            }
            return total;
        }

        public List<Products> get(String collectie, String merk)
        {
                MongoCollection<Products> moederborden = connect("Products").GetCollection<Products>(collectie);
                var query1 = moederborden.Find(Query.Matches("Title", BsonRegularExpression.Create(new Regex(merk, RegexOptions.IgnoreCase))));
                var query2 = moederborden.Find(Query.Matches("description", BsonRegularExpression.Create(new Regex(merk, RegexOptions.IgnoreCase))));
                List<Products> query1list = query1.ToList();
                List<Products> query2list = query2.ToList();
                query1list.AddRange(query2list);
                List<Products> productsList = new List<Products>();
                productsList.AddRange(query1list.Distinct());
                return productsList;
        }

        public List<Prijs> getPrices(String merk)
        {
                MongoCollection<Prijs> moederborden = connect("Prijzen").GetCollection<Prijs>("Prijzen");
                var query1 = moederborden.Find(Query.Matches("titles", BsonRegularExpression.Create(new Regex(merk, RegexOptions.IgnoreCase))));
                List<Prijs> productsList = new List<Prijs>();
                List<Prijs> query1list = query1.ToList();
                productsList.AddRange(query1list.Distinct());
                return productsList;
        }
    }
    
}
