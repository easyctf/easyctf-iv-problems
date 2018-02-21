using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.IO.Compression;
using System.Text;
using System.Reflection;

namespace payload
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            List<byte> dat = new List<byte>();
            for (int i = 0; i < args.Length; ++i)
                dat.Add(byte.Parse(args[i]));
            var ms = new MemoryStream(dat.ToArray());
            GZipStream gz = new GZipStream(ms, CompressionMode.Decompress);
            byte[] buff = new byte[0x100];
            List<byte> total = new List<byte>();
            int cnt = 0;
            do
            {
                cnt = gz.Read(buff, 0, 0x100);
                total.AddRange(buff.Take(cnt));
            }
            while (cnt != 0);

            Assembly.Load(total.ToArray())
                .EntryPoint.Invoke(null, null);
        }
    }
}
