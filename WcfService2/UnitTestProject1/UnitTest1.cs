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
            Assert.AreEqual(true,database.GetCollection("files2").Exists());
        }

        [TestMethod]
        public void checkResult()
            //Kijkt of er wel wat wordt teruggegeven
        {
            Service1 service = new Service1();
            Assert.IsTrue(service.getMoederbordAMD().Count > 0);
        }
    }
}
