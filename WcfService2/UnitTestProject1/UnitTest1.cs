using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using WcfService2;
using MongoDB.Driver;
using MongoDB.Bson;
using MongoDB.Driver.Builders;
using MongoDB.Driver.GridFS;
using MongoDB.Driver.Linq;
using MongoDB;
using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson.IO;
using NUnit;
using System.Diagnostics;

namespace UnitTestProject1
{
    [TestClass]
    public class UnitTest1
    {
        public String[] fillArray()
        {
            String[] collections = new String[12];
            collections[0] = "Behuizingen";
            collections[1] = "Controllers";
            collections[2] = "Energie";
            collections[3] = "Geheugen";
            collections[4] = "Geluidskaarten";
            collections[5] = "Hardeschijf";
            collections[6] = "Koeling";
            collections[7] = "Moederborden";
            collections[8] = "Netwerk";
            collections[9] = "OptischeDrivers";
            collections[10] = "NetwerkOpslag";
            collections[11] = "Processoren";
            return collections;
        }
       

        [TestMethod]
        public void testConnection()
            //Kijkt of er succesvol verbonden wordt met de database
        {
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            Assert.IsNotNull(server.GetDatabaseNames());
        }

        [TestMethod]
        public void getCollection()
            //Kijkt of de collectie wel bestaat
        {
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            MongoDatabase database = server.GetDatabase("Products");
            for (int x = 0; x < 12; x++)
            {
                Assert.AreEqual(true, database.GetCollection(fillArray()[x]).Exists());
            }
        }

        [TestMethod]
        public void checkResult()
            //Kijkt of er wel wat wordt teruggegeven
        {
            Service1 service = new Service1();
            Assert.IsTrue(service.getAllProducts().Count > 0);
        }
    }
}
